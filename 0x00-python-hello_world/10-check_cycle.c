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
	if (list)
		while ((temp = temp->next)
		       if (temp == list)
			       return (1);
	return (0);
}
