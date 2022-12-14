#include "lists.h"
/**
 *check_cycle - checks if there is  cycle ina linked list
 *
 *@list: the linked list to check
 *Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	temp = list;
	while (temp)
	{
		if (temp->next >= temp)
			return (1);
		temp = temp->next;
	}
	return (0);
}
